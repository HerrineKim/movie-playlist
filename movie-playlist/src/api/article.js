import api from "./api"

const END_POINT = "articles"

export default {
  all() {
    return api({
      method: "get",
      url: `${END_POINT}/`,
    })
  },
  detail(id) {
    return api({
      method: "get",
      url: `${END_POINT}/${id}/`,
    })
  },
  create(data) {
    return api({
      method: "post",
      url: `${END_POINT}/`,
      data: data,
    })
  },
  update(id, data) {
    return api({
      method: "put",
      url: `${END_POINT}/${id}/`,
      data: data,
    })
  },
  delete(id) {
    return api({
      method: "delete",
      url: `${END_POINT}/${id}/`,
    });
  },
  like(id) {
    return api({
      method: "post",
      url: `${END_POINT}/${id}/like/`,
    })
  },
}
