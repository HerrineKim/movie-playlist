import movie from "@/api/movie"
import router from "@/router"

export default {
  state: {
    genre_movies: { id: "", movies: [] },
    moodtag_movies: { id: "", movies: [] },
    casetag_movies: { id: "", movies: [] },
  },
  getters: {
    genre_movies: (state) => state.genre_movies,
    moodtag_movies: (state) => state.moodtag_movies,
    casetag_movies: (state) => state.casetag_movies,
  },
  mutations: {
    SET_GENRE_MOVIES: (state, genre_movies) => (state.genre_movies = genre_movies),
    SET_MOODTAG_MOVIES: (state, moodtag_movies) => (state.moodtag_movies = moodtag_movies),
    SET_CASETAG_MOVIES: (state, casetag_movies) => (state.casetag_movies = casetag_movies),
  },
  actions: {
    fetchGenreMovies({ commit }, { genrePk }) {
      movie
        .genre(genrePk)
        .then((res) => {
          commit("SET_GENRE_MOVIES", res.data)
          // console.log(res.data)
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    fetchMoodtagMovies({ commit }, { moodtagPk }) {
      movie
        .genre(moodtagPk)
        .then((res) => {
          commit("SET_MOODTAG_MOVIES", res.data)
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    fetchCasetagMovies({ commit }, { casetagPk }) {
      movie
        .genre(casetagPk)
        .then((res) => {
          commit("SET_CASETAG_MOVIES", res.data)
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
  }
}