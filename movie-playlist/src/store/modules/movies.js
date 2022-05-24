import movie from "@/api/movie"
import router from "@/router"

export default {
  state: {
    actors: [],
    actor: { name: "", profile_path: "", movies: []},
    movie: {},
    recommendation: [],
    similar: []
  },
  getters: {
    actors: (state) => state.actors,
    actor: (state) => state.actor,
    article: (state) => state.article,
    movie: (state) => state.movie,
    recommendation: (state) => state.recommendation,
    similar: (state) => state.similar
  },
  mutations: {
    SET_ACTORS: (state, actors) => (state.actors = actors),
    SET_ACTOR: (state, actor) => (state.actor = actor),
    SET_MOVIE: (state, movie) => (state.movie = movie),
    SET_RECOMMENDATION: (state, recommendation) => (state.recommendation = recommendation),
    SET_SIMILAR: (state, similar) => (state.similar = similar)
  },
  actions: {
    fetchActors({ commit }) {
      movie
        .actors()
        .then((res) => {
          commit("SET_ACTORS", res.data);
          console.log(res.data)
        })
        .catch((err) => console.error(err.response));
    },
    fetchActor({ commit }, { actorPk }) {
      movie
        .actor(actorPk)
        .then((res) => {
          commit("SET_ACTOR", res.data);
          console.log(res.data)
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
    movieLike({ commit }, { moviePk }) {
      movie
        .movie_like(moviePk)
        .then((res) => {
          commit("SET_MOVIE", res.data);
        })
        .catch((err) => console.error(err.response))
    },
    recommendation({ commit }, { userPk }) {
      movie
        .recommendation(userPk)
        .then((res) => {
          commit("SET_RECOMMENDATION", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    },
    similar({ commit }, { moviePk }) {
      movie
        .similar(moviePk)
        .then((res) => {
          commit("SET_SIMILAR", res.data);
        })
        .catch((err) => {
          if (err.response.status === 404) {
            router.push({ name: "NotFound404" });
          }
        })
    }
  }
}