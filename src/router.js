import Vue from 'vue'
import VueRouter from 'vue-router'
import listArticle from './views/listArticle.vue'
import createArticle from './views/createArticle.vue'
import editArticle from './views/editArticle.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: '/articles/index'
  },
  {
    path: '/articles/index',
    name: 'list-article',
    component: listArticle
  },
  {
    path: '/articles/create',
    name: 'create-article',
    component: createArticle
  },
  {
    path: '/articles/:id/edit',
    name: 'edit-article',
    component: editArticle
  },
]

const router = new VueRouter({
  routes
})

export default router
