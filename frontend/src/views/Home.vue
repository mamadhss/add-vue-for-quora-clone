<template>
  <div class="home">
    <div class="container">

      <div v-for="question in questions" :key="question.pk">
        <p class="mb-0">Posted by:
          <span>{{question.author}}</span>
        </p>
        <h2>
          <router-link
            :to="{name:'question',params: {slug:question.slug}}"
          >{{question.content}}
          </router-link>
        </h2>
        <p>Answers : {{question.answers_count}}</p>
        <hr>
      </div>
     
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import { apiService } from "../common/api.service.js";

export default {
  name: "Home",
  data() {
    return {
      questions:[]
    }

  },
  methods: {
    getQuestions() {
      let endpoint = "api/questions/";
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results);
        })
       
    }
  },
  created() {
    this.getQuestions()
    
  }
};
</script>
