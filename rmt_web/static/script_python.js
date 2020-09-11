var myCodeMirror = CodeMirror.fromTextArea(document.getElementById("code"), {
  lineNumbers: true,
  matchBrackets: true,
  mode: 'python',
  indentUnit: 4,
  version: 3
});
