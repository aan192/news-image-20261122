import * as fs from 'fs';
import * as path from 'path';

function main() {
    const src = path.resolve('entry.png');
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
