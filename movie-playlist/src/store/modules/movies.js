import movie from "@/api/movie"
import router from "@/router"

export default {
  state: {
    actors: [],
    actor: { name: "", profile_path: "", movies: []},
    movie: {},
    recommendationMovies: [],
    similarMovies: [],
    search: [],
    rating: 1
  },
  getters: {
    actors: (state) => state.actors,
    actor: (state) => state.actor,
    article: (state) => state.article,
    movie: (state) => state.movie,
    recommendationMovies: (state) => state.recommendationMovies,
    similarMovies: (state) => state.similarMovies,
    search: (state) => state.search,
    rating: (state) => state.rating
  },
  mutations: {
    SET_ACTORS: (state, actors) => (state.actors = actors),
    SET_ACTOR: (state, actor) => (state.actor = actor),
    SET_MOVIE: (state, movie) => (state.movie = movie),
    SET_RECOMMENDATION_MOVIES: (state, recommendation) => (state.recommendationMovies = recommendation),
    SET_SIMILAR_MOVIES: (state, similar) => (state.similarMovies = similar),
    SET_SEARCH: (state, search) => (state.search = search),
    SET_RATING: (state, rating) => (state.rating = rating)
  },
  actions: {
    fetchActors({ commit }) {
      movie
        .actors()
        .then((res) => {
          commit("SET_ACTORS", res.data);
        })
        .catch((err) => console.error(err.response));
    },
    fetchActor({ commit }, {actorPk}) {
      movie
        .actor(actorPk)
        .then((res) => {
          commit("SET_ACTOR", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404"});
          }
        })
    },
    fetchMovie({ commit }, { moviePk }) {
      movie
        .movie(moviePk)
        .then((res) => {
          commit("SET_MOVIE", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    movieLike({ commit }, moviePk) {
      movie
        .movie_like(moviePk)
        .then((res) => {
          commit("SET_MOVIE", res.data);
        })
        .catch((err) => console.error(err.response))
    },
    recommendation({ commit }, {userPk}) {
      movie
        .recommendation(userPk)
        .then((res) => {
          commit("SET_RECOMMENDATION_MOVIES", res.data);
          console.log(res.data)
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    similar({ commit }, {moviePk}) {
      movie
        .similar(moviePk)
        .then((res) => {
          commit("SET_SIMILAR_MOVIES", res.data);
          // console.log(res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    search({ commit }, movieName) {
      movie
        .search(movieName)
        .then((res) => {
          commit("SET_SEARCH", res.data);
          console.log(res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    // 평점
    create_rating({ commit }, { moviePk, rate }) {
      const body = {rate}
      movie
        .create_rating(moviePk, body)
        .then((res) => {
          commit("SET_RATING", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    delete_rating({ commit }, moviePk, ratingPk) {
      movie
        .delete_rating(moviePk, ratingPk)
        .then((res) => {
          commit("SET_RATING", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    }
  }
}