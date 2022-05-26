import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import FirstView from '../views/FirstView.vue'
import HashtagView from '../views/HashtagView.vue'
import ActorsView from '../views/ActorsView.vue'
import ArticleListView from '../views/ArticleListView.vue'
import SignupView from '../views/SignupView.vue'
import NotFound404 from '../views/NotFound404.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SearchView from '../views/SearchView.vue'
import ArticleNewView from '../views/ArticleNewView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import ArticleEditView from '../views/ArticleEditView.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ProfileView from '../views/ProfileView.vue'
import ActorView from '../views/ActorView.vue'
import OstView from '../views/OstView.vue'

Vue.use(VueRouter)

const routes = [

  // 홈 및 초기화면
  {
    path: '/',
    name: 'HomeView',
    component: HomeView, 
  },
  {
    path: '/first',
    name: 'first',
    component: FirstView
  },

  // 해시태그 영화 추천
  {
    path: '/hashtag',
    name: 'hashtag',
    component: HashtagView
  },

  // 배우 검색
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

  // Community
  {
    path: '/articles',
    name: 'articles',
    component: ArticleListView,
  },
  {
    path: '/articles/new',
    name: 'articleNew',
    component: ArticleNewView,
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView,
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView,
  },

  // 영화 검색
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

  // OST
  {
    path: '/OST',
    name: 'OST',
    component: OstView
  },

  // Accounts, 404
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
    },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
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

// Navigation Guard
router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  // Login 필요 없는 route의 name
  const noAuthPages = ['login', 'signup', 'HomeView',]

  // 현재 이동하고자 하는 페이지가 Authentication이 필요한가?
  const isAuthRequired = !noAuthPages.includes(to.name)

  // Auth가 필요한데, 로그인 되어있지 않다면?
  if (isAuthRequired && !isLoggedIn) {
    alert('로그인하셔야 서비스를 이용하실 수 있습니다.')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'HomeView'})
  }
})

export default router
