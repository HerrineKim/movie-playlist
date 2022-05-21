
import axios from 'axios'


const KOR_URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
const KOR_KEY = '66c2caa77d9f0b8b981e4940228bf4ac'
// const today = new Date().toISOString().substring(0,10).replace(/-/g,'');

export default {
  state: {
    boxoffice: [],
  },
  getters: {
    boxoffice: (state) => state.boxoffice,
  },
  mutations: {
    FETCH_BOXOFFICE (state, boxoffice) {
      state.boxoffice = boxoffice
    },
  },
  actions: {
    fetchBoxoffice ({ commit }) {
      axios ({
        method: 'get',
        url : KOR_URL,
        params: {
          key: KOR_KEY,
          targetDt: '20220103',
        },
      })
      .then(res => {
        commit('FETCH_BOXOFFICE', res.data.boxOfficeResult.dailyBoxOfficeList)
        console.log(res.data.boxOfficeResult.dailyBoxOfficeList)
      })
      .catch(err => console.log(err))
    },
  },
}