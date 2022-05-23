import Vue from 'vue'
import Vuex from 'vuex'

// import articles from './modules/articles'
import accounts from './modules/accounts'
import home from './modules/home'
import articles from './modules/articles'
import movies from './modules/movies'
import tags from './modules/tags'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, home, articles, movies, tags },
})
