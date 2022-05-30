import api from "./api"

export default {
  // actor: 배우 목록 전체
  actors() {
    return api({
      method: "get",
      url: "movies/actors/",
    })
  },
  actor(id) {
    return api({
      method: "get",
      url: `movies/actors/${id}`,
    })
  },
  // genre
  genre(id) {
    return api({
      method: "get",
      url: `movies/genre/${id}`,
    })
  },
  // tags
  moodtag(id) {
    return api({
      method: "get",
      url: `movies/moodtag/${id}`,
    })
  },
  casetag(id) {
    return api({
      method: "get",
      url: `movies/casetag/${id}`,
    })
  },
  // movie
  movie(id) {
    return api({
      method: "get",
      url: `movies/${id}`,
    })
  },
  movie_like(id) {
    return api({
      method: "post",
      url: `movies/${id}/like/`,
    })
  },
  recommendation(id) {
    return api({
      method: "get",
      url: `movies/${id}/recommendation`,
    })
  },
  similar(id) {
    return api({
      method: "get",
      url: `movies/${id}/similar`,
    })
  },
  search(movie_name) {
    return api({
      method: "get",
      url: `movies/${movie_name}`,
    })
  },
  create_rating(moviePk, data) {
    return api({
      method: "post",
      url: `movies/${moviePk}/rating/`,
      data: data
    })
  },
  update_rating(moviePk, ratingPk, data) {
    return api({
      method: "post",
      url: `movies/${moviePk}/rating/${ratingPk}`,
      data: data,
    })
  },
  delete_rating(moviePk, ratingPk) {
    return api({
      method: "delete",
      url: `movies/${moviePk}/rating/${ratingPk}`,
    })
  },
}