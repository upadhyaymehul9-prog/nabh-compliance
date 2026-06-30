#!/usr/bin/env node
/**
 * Renders marketing/video/accredready-promo.html to MP4 via Playwright screen recording.
 * Usage: node scripts/render-promo-video.js
 */
const path = require("path");
const fs = require("fs");
const { chromium } = require("playwright");

const DURATION_MS = 36000; // match HTML animation (~36s)
const WIDTH = 1920;
const HEIGHT = 1080;
const HTML = path.resolve(__dirname, "../marketing/video/accredready-promo.html");
const OUT_DIR = path.resolve(__dirname, "../marketing/video/output");

async function main() {
  if (!fs.existsSync(HTML)) {
    console.error("Missing:", HTML);
    process.exit(1);
  }
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const browser = await chromium.launch({
    headless: true,
    args: ["--no-sandbox", "--disable-dev-shm-usage"],
  });

  const context = await browser.newContext({
    viewport: { width: WIDTH, height: HEIGHT },
    deviceScaleFactor: 1,
    recordVideo: {
      dir: OUT_DIR,
      size: { width: WIDTH, height: HEIGHT },
    },
  });

  const page = await context.newPage();
  await page.goto(`file://${HTML}`, { waitUntil: "networkidle" });
  await page.waitForTimeout(DURATION_MS);

  const video = page.video();
  await context.close();
  await browser.close();

  if (!video) {
    console.error("No video recorded");
    process.exit(1);
  }

  const webmPath = await video.path();
  const mp4Path = path.join(OUT_DIR, "accredready-promo-1080p.mp4");

  const { execSync } = require("child_process");
  execSync(
    `ffmpeg -y -i "${webmPath}" -c:v libx264 -pix_fmt yuv420p -crf 20 -preset medium -movflags +faststart "${mp4Path}"`,
    { stdio: "inherit" }
  );

  // Vertical crop for Reels (optional second output)
  const verticalPath = path.join(OUT_DIR, "accredready-promo-vertical.mp4");
  execSync(
    `ffmpeg -y -i "${mp4Path}" -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" -c:v libx264 -pix_fmt yuv420p -crf 20 -preset medium -movflags +faststart "${verticalPath}"`,
    { stdio: "inherit" }
  );

  console.log("\n✓ Horizontal (YouTube/LinkedIn):", mp4Path);
  console.log("✓ Vertical (Reels/Shorts):", verticalPath);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
