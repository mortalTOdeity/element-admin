<template>
  <div>
    <el-table :data="articles">
      <el-table-column prop="title"
                       label="ip"
                       width="140">
      </el-table-column>
      <el-table-column prop="body"
                       label="主机名"
                       width="220">
      </el-table-column>
      <el-table-column prop="address"
                       label="位置"
                       width="140">
      </el-table-column>
      <el-table-column fixed="right"
                       label="操作">
        <template slot-scope="scope">
          <el-button @click="edit(scope.row._id)"
                     type="text"
                     size="small">编辑</el-button>
          <el-button @click="remove(scope.row._id)"
                     type="text"
                     size="small">删除</el-button>
          <el-button @click="postTest()"
                     type="text"
                     size="small">post测试</el-button>
          <el-button type="primary"
                     @click="test2()"
                     size="small">测试2</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      articles: []
    }
  },
  methods: {
    fetch () {
      this.$http.get('articles').then(res => {
        this.articles = res.data
      })
    },
    edit (id) {
      this.$router.push(`/articles/${id}/edit`)
    },
    remove (id) {
      this.$http.delete(`articles/${id}`).then(() => {
        this.$message({
          message: '机器删除成功',
          type: 'success'
        })
        this.fetch()
      })
    },
    postTest () {
      this.$http.get('/buttonClicked').then(() => {
        console.log('test')
        alert('你在测试！！')
      })
    },
    test2 () {
      this.$http.get('/buttonChecked').then(() => {
        console.log('test2')
        alert('测试2！')
      })
    },
    created () {
      this.fetch()
    }
  }
}
</script>