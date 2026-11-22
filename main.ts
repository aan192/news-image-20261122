import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function main() {
    const src = path.join(__dirname, 'entry.png');
    const destDir = '/output';
    const dest = path.join(destDir, 'entry.png');

    if (!fs.existsSync(src)) {
        console.error(`Source file not found: ${src}`);
        process.exit(1);
    }

    if (!fs.existsSync(destDir)) {
        fs.mkdirSync(destDir, { recursive: true });
        console.log(`Created directory: ${destDir}`);
    }

    fs.copyFileSync(src, dest);
    console.log(`Successfully copied ${src} to ${dest}`);
}

main();
