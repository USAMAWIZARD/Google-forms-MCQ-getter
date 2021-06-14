app=require("express");
server=app();
const spawn = require("child_process").spawn;
server.get("/:examLink",(req,res)=>{
const pythonProcess = spawn('python',["./ScrapQuestions.py",req.params.examLink]);
console.log("sdf")
pythonProcess.stdout.on('data', (data) => {
console.log(data)
res.json(`${data}`)
res.end()
});

});


server.listen(
    3000
);