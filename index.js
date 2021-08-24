var express = require("express");
var app = express();

const spawn = require("child_process").spawn;
const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));
app.post("/", (req, res) => {
  const pythonProcess = spawn("py", ["./ScrapQuestions.py", req.body.url]);
  pythonProcess.stdout.on("data", (data) => {
    parseddata = JsonParser(data.toString());
    res.json(parseddata);
  });
  pythonProcess.on("error", (err) => console.log(err));
});
JsonParser = (e) => {
  arrofobb = [];
  data = eval(e)[0];
  let count = 0;
  while (typeof data[count] != "object") {
    count += 1;
  }
  data = data[count];
  for (let i = 0; i < data.length; i++) {
    temp = {};
    optionpos = data[i].length - 1;
    if (
      typeof data[i][optionpos][0] == "object" &&
      data[i][optionpos][0][1] !== undefined
    ) {
      option = [];
      temp.question = data[i][1];

      for (let j = 0; j < data[i][optionpos][0][1].length; j++) {
        option.push(data[i][optionpos][0][1][j][0]);
        temp.option = option;
      }
      arrofobb.push(temp);
    }
  }
  return arrofobb;
};
port = 3000;
app.listen(port, () => console.log(`listening on ${port}`));
