import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FirstView from '../views/FirstView.vue'
import HashtagView from '../views/HashtagView.vue'
import ActorsView from '../views/ActorsView.vue'
import CommunityView from '../views/CommunityView.vue'
import SignupView from '../views/SignupView.vue'
import NotFound404 from '../views/NotFound404.vue'
import LogoutView from '../views/LogoutView.vue'
import SearchView from '../views/SearchView.vue'
import ArticleNewView from '../views/ArticleNewView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import ArticleEditView from '../views/ArticleEditView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ProfileView from '../views/ProfileView.vue'
import ActorView from '../views/ActorView.vue'

Vue.use(VueRouter)

const routes = [
  {
  path: '/login',
  name: 'login',
  component: HomeView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
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
  {
    path: '/actors/:actorPk',
    name: 'actor',
    component: ActorView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/community/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/community/:articlePk',
    name: 'articleDetail',
    component: ArticleDetailView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/search/:moviePk',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
