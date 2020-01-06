<template>
  <el-form @submit.native.prevent="saveArticle"
           ref="form"
           :model="article"
           label-width="80px">
    <el-form-item label="机器名称">
      <el-input v-model="article.title"></el-input>
    </el-form-item>
    <el-form-item label="机器信息">
      <el-input type="textarea"
                v-model="article.body"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary"
                 native-type="submit">立即创建</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data () {
    return {
      article: {}
    }
  },
  methods: {
    saveArticle () {
      this.$http.post('/articles', this.article).then(() => {
        this.$message({
          message: '机器创建成功',
          type: 'success'
        })
        this.$router.push('/articles/index')
      })
    },
    fetch() {
      this.$http.get(`articles/${this.$route.params.id}`).then(res => {
        this.article = res.data
      })
    },
    created() {
      this.fetch()
    }
  }
}
</script>