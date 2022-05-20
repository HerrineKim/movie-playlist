import api from "./api"

const END_POINT = "accounts"

export default {
  login(data) {
    return api({
      method: "post",
      url: `${END_POINT}/login/`,
      data: data,
    })
  },
  logout() {
    return api({
      method: "post",
      url: `${END_POINT}/logout/`,
    })
  },
  signup(data) {
    return api({
      method: "post",
      url: `${END_POINT}/signup/`,
      data: data,
    })
  },
  currentUser() {
    return api({
      method: "get",
      url: `${END_POINT}/user/`,
    })
  },
  profile(username) {
    return api({
      method: "get",
      url: `${END_POINT}/profile/${username}/`,
    })
  },
}
