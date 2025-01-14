#!/usr/bin/env cwltool

label: run-xcell-tool
id: run-xcell-tool
cwlVersion: v1.2
class: CommandLineTool
baseCommand: Rscript

arguments:
  - --vanilla
  - /bin/xcell.r

requirements:
   - class: DockerRequirement
     dockerPull: tumordeconv/xcell
   - class: InlineJavascriptRequirement

inputs:
  expression:
    type: File
    inputBinding:
      position: 1
  signature:
    type: ["null", File]  # Allows the input to be null (optional)
    inputBinding:
      position: 2
      valueFrom: "$(self ? self.path : '')"  # Only include the parameter if it's provided

outputs:
  deconvoluted:
    type: File
    outputBinding:
      glob: "deconvoluted.tsv"
      outputEval: |
        ${
          var mat = inputs.signature ? inputs.signature.nameroot : "default";
          var cancer = inputs.expression.nameroot;
          var name = cancer + '-xcell-' + mat + '.tsv';
          self[0].basename = name;
          return self[0];
        }
