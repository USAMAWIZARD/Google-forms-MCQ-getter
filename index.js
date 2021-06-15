app=require("express");
server=app();

const spawn = require("child_process").spawn;
const bodyParser= require('body-parser');
server.use(bodyParser.urlencoded({extended:true}))
server.post("/",(req,res)=>{
console.log(req.body.examLink)
const pythonProcess = spawn('python3',["./ScrapQuestions.py",req.body.examLink]);

pythonProcess.stdout.on('data', (data) => {
res.send(`${data}`)
console.log(`${data}`)
res.end()
});

});


server.listen(
    3020
);
