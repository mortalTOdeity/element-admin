const express = require('express')

const app = express()

const fs = require('fs')

const exec = require('child_process').exec

app.use(require('cors')())
app.use(express.json())

const mongoose = require('mongoose')

mongoose.connect('mongodb://localhost:27017/element-admin', {
  useNewUrlParser: true,
  useFindAndModify: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
})

const Article = mongoose.model('Article', new mongoose.Schema({
  title: { type: String },
  body: { type: String }
}))


// 展示
app.get('/', async (req, res) => {
  res.send('index')
})


// 新增
app.post('/api/articles', async (req, res) => {
  const article = await Article.create(req.body)
  res.send(article)
})

// 显示
app.get('/api/articles', async (req, res) => {
  const articles = await Article.find()
  res.send(articles)
})

// post测试

// app.get('/api/buttonClicked', async (req, res) => {
//   const mark = Math.random() * 9999999
//   fs.mkdir('/Users/180563/Desktop/testfolder/test' + mark, function (err) {
//     if (err) {
//       console.error(err)
//     }
//   })
//   console.log('testout')
//   res.send('asd')
// })

// 新建文件夹测试
app.get('/api/buttonClicked', async (req, res) => {
  const mark = Math.random() * 9999999
  fs.mkdir('/Users/180563/Desktop/testfolder/test' + mark, function (err) {
    if (err) {
      console.error(err)
    }
  })
  console.log('testout')
  res.send('asd')
})

// 脚本测试
app.get('/api/buttonChecked', async (req, res) => {
  exec('python py_playbook.py', function (err, stdout, stderr) {
    if (err) {
      console.error(err)
    }
    console.log(stdout)
  })
  res.send(200)
})

// 删除

app.delete('/api/articles/:id', async (req, res) => {
  await Article.findByIdAndDelete(req.params.id)
  res.send({
    status: true
  })
})


// 详情

app.get('/api/articles/:id', async (req, res) => {
  const article = await Article.findById(req.params.id)
  res.send(article)
})



app.listen(3001, () => {
  console.log('http://localhost:3001')
})
