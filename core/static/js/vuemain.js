var csrftoken = Cookies.get('csrftoken')
Vue.http.headers.common['X-CSRFTOKEN'] = csrftoken
Vue.http.options.root = '/';

const requestUserPk = parseInt(document.getElementById('request-user-pk').value)
const requestUser = document.getElementById('request-user').value

const vueMain = new Vue({
    el: '#vue-main',
    delimiters: ['${', '}'],
    data: {
        requestUserPk: requestUserPk,
        requestUser: requestUser,
    },
    mounted: function () {

    },
    methods: {

    }
}