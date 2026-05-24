/**
 * make-favicon.js
 * Converts public/logo192.png → public/favicon.ico
 * Sizes embedded: 16x16, 32x32, 48x48
 * Uses only fast-png (already in node_modules) + Node.js stdlib.
 * ICO entries use 32-bit ARGB BMP (no PNG embedding) for max compatibility.
 */

const { decode } = require('fast-png');
const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, '..', 'public', 'logo192.png');
const dst = path.join(__dirname, '..', 'public', 'favicon.ico');

const png = decode(fs.readFileSync(src));
const { width: SW, height: SH, data: srcData, channels } = png;

// ── Bilinear resize ──────────────────────────────────────────────────────────
function resize(srcData, srcW, srcH, dstW, dstH, channels) {
  const dst = new Uint8Array(dstW * dstH * 4);
  const xRatio = srcW / dstW;
  const yRatio = srcH / dstH;

  for (let y = 0; y < dstH; y++) {
    for (let x = 0; x < dstW; x++) {
      const srcX = x * xRatio;
      const srcY = y * yRatio;
      const x0 = Math.floor(srcX), x1 = Math.min(x0 + 1, srcW - 1);
      const y0 = Math.floor(srcY), y1 = Math.min(y0 + 1, srcH - 1);
      const xFrac = srcX - x0, yFrac = srcY - y0;

      const dstIdx = (y * dstW + x) * 4;
      for (let c = 0; c < 4; c++) {
        const ch = c < channels ? c : (channels === 3 && c === 3 ? -1 : c);
        const getP = (px, py) => ch === -1 ? 255 : srcData[(py * srcW + px) * channels + ch];
        const top    = getP(x0, y0) * (1 - xFrac) + getP(x1, y0) * xFrac;
        const bottom = getP(x0, y1) * (1 - xFrac) + getP(x1, y1) * xFrac;
        dst[dstIdx + c] = Math.round(top * (1 - yFrac) + bottom * yFrac);
      }
    }
  }
  return dst;
}

// ── Build BMP payload for one size ──────────────────────────────────────────
// ICO uses a BITMAPINFOHEADER + XOR mask (BGRA) + AND mask (1-bit)
function buildBmpPayload(rgba, size) {
  const headerSize = 40;
  const rowSize = size * 4;                    // 32 bpp, no padding needed
  const xorSize = rowSize * size;
  const andRowBytes = Math.ceil(size / 8);
  const andRowPadded = Math.ceil(andRowBytes / 4) * 4;
  const andSize = andRowPadded * size;

  const buf = Buffer.alloc(headerSize + xorSize + andSize);
  let off = 0;

  // BITMAPINFOHEADER (height = 2*size because ICO stacks XOR+AND)
  buf.writeUInt32LE(40, off);          off += 4;  // biSize
  buf.writeInt32LE(size, off);         off += 4;  // biWidth
  buf.writeInt32LE(size * 2, off);     off += 4;  // biHeight (doubled)
  buf.writeUInt16LE(1, off);           off += 2;  // biPlanes
  buf.writeUInt16LE(32, off);          off += 2;  // biBitCount
  buf.writeUInt32LE(0, off);           off += 4;  // biCompression (BI_RGB)
  buf.writeUInt32LE(xorSize, off);     off += 4;  // biSizeImage
  buf.writeInt32LE(0, off);            off += 4;  // biXPelsPerMeter
  buf.writeInt32LE(0, off);            off += 4;  // biYPelsPerMeter
  buf.writeUInt32LE(0, off);           off += 4;  // biClrUsed
  buf.writeUInt32LE(0, off);           off += 4;  // biClrImportant

  // XOR mask: BGRA rows, bottom-up
  for (let y = size - 1; y >= 0; y--) {
    for (let x = 0; x < size; x++) {
      const src = (y * size + x) * 4;
      buf[off++] = rgba[src + 2]; // B
      buf[off++] = rgba[src + 1]; // G
      buf[off++] = rgba[src + 0]; // R
      buf[off++] = rgba[src + 3]; // A
    }
  }

  // AND mask: 1 bit per pixel, bottom-up, row-padded to 4 bytes
  // Pixel is transparent in AND mask only if alpha == 0
  for (let y = size - 1; y >= 0; y--) {
    for (let bx = 0; bx < andRowPadded; bx++) {
      let byte = 0;
      for (let bit = 0; bit < 8; bit++) {
        const x = bx * 8 + bit;
        if (x < size) {
          const alpha = rgba[(y * size + x) * 4 + 3];
          if (alpha === 0) byte |= (0x80 >> bit);
        }
      }
      buf[off++] = byte;
    }
  }

  return buf;
}

// ── Assemble ICO ─────────────────────────────────────────────────────────────
const SIZES = [16, 32, 48];
const payloads = SIZES.map(sz => {
  const rgba = resize(srcData, SW, SH, sz, sz, channels);
  return buildBmpPayload(rgba, sz);
});

const HEADER = 6;
const ENTRY  = 16;
const dirEnd = HEADER + SIZES.length * ENTRY;
let dataOffset = dirEnd;

const headerBuf = Buffer.alloc(HEADER);
headerBuf.writeUInt16LE(0, 0);           // reserved
headerBuf.writeUInt16LE(1, 2);           // type: ICO
headerBuf.writeUInt16LE(SIZES.length, 4);

const dirBuf = Buffer.concat(payloads.map((payload, i) => {
  const sz = SIZES[i];
  const e = Buffer.alloc(ENTRY);
  e.writeUInt8(sz, 0);                   // width  (0 = 256)
  e.writeUInt8(sz, 1);                   // height
  e.writeUInt8(0, 2);                    // color count
  e.writeUInt8(0, 3);                    // reserved
  e.writeUInt16LE(1, 4);                 // planes
  e.writeUInt16LE(32, 6);                // bit count
  e.writeUInt32LE(payload.length, 8);    // size
  e.writeUInt32LE(dataOffset, 12);       // offset
  dataOffset += payload.length;
  return e;
}));

const ico = Buffer.concat([headerBuf, dirBuf, ...payloads]);
fs.writeFileSync(dst, ico);
console.log(`favicon.ico written: ${ico.length} bytes (16×16, 32×32, 48×48)`);
