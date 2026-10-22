import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
const final='renders/raitec-ki-kostenentwicklung-9x16.mp4';
const temp='renders/raitec-ki-kostenentwicklung-9x16-normalized.mp4';
execFileSync('ffmpeg',['-y','-hide_banner','-loglevel','error','-i',final,'-c:v','copy','-af','loudnorm=I=-16:TP=-1.5:LRA=7','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',temp],{stdio:'inherit'});
fs.renameSync(temp,final);
console.log('Final audio normalized to -16 LUFS; picture stream copied unchanged.');
