<template>
    <div class="container mt-2">
        <h1>Ask A Question</h1>
        <form @submit.prevent="onSubmit" >
            <textarea 
            v-model="question_body"
            class="form-control"
            placeholder="what do you want to ask"
            rows="3"
            ></textarea>
            <br>
            <button
                type="submit"
                class="btn btn-success"
                >Publish
            </button>
        </form>
        <p v-if="error" class=" muted mt-2">{{error}}</p>

    </div>
</template>


<script>
import { apiService } from "../common/api.service.js";
export default {
    name:"QuestionEditor",
    data() {
        return {
            question_body:null,
            error:null

        }
        
    },
    methods: {
        onSubmit() {
            if (!this.question_body) {
                this.error = "you cant send empty question"

            } else if(this.question_body.length > 240) {
                this.error = "Ensure field no more than 240 char";
            } else {
                let endpoint = "api/questions/";
                let method = "POST";
                apiService(endpoint,method,{content:this.question_body})
                    .then(question_data => {
                        this.$router.push({
                            name:'question',
                            params: {slug: question_data.slug}
                        })
                    })
            }
            

        }

    },

    created() {
        document.title = "Editor - QuestionTime";
    }
    
}
</script>