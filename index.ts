
import express from "express";
import {router} from "express-file-routing";

const app = express();
const port = 3000;

app.use("/", await router())

app.listen(port, () => {
  console.log(`[master-server]: Server is running at http://localhost:${port} 🚀`);
});
