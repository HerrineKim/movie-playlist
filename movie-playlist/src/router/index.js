import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FirstView from '../views/FirstView.vue'
import HashtagView from '../views/HashtagView.vue'
import ActorsView from '../views/ActorsView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/first',
    name: 'first',
    component: FirstView
  },
  {
    path: '/hashtag',
    name: 'hashtag',
    component: HashtagView
  },
  {
    path: '/actors',
    name: 'actors',
    component: ActorsView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
