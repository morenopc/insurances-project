var apiURL = 'api/v1/risks/';
var app = new Vue({
  el: "#app",

  data:{
    risks: []
  },

  created: function () {
    this.fetchData();
  },

  methods: {
    fetchData: function() {
            axios.get(apiURL)
              .then(response => {this.risks = response.data})
          }
  }
})
