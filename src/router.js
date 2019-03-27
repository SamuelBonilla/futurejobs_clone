import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import PostJob from './views/PostJob.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/post_job',
      name: 'post_job',
      component: PostJob
    }
  ]
})
