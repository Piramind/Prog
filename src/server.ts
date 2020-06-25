import fastify from "fastify";
let server = fastify();

server.post('/test/', (req, res)=>
{
    let data = req.body;
    res.send(data.message)
})
server.listen(3000, 'localhost')
    .then(adress => { })
    .catch(error => console.error(error));