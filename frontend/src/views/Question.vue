<template>
    <div class="single-question m2-2">
        <div class="container">
            <h1>{{question.content}}</h1>
            <p class="mb-0"> Posted by:
                <span class="author-name">{{question.author}}</span>
            </p>
            <p>{{question.created_at}}</p>
        
            <hr>
            <div v-if="userHasAnswered">
                <p class="asnwer-added">you have written an answer!</p>
            </div>
            <div v-else-if="showForm">
                <form class="card" @submit.prevent="onSubmit">
                    <div class="card-header px-3">
                        Answer the Question
                    </div>
                    <div class="card-block">
                        <textarea
                        v-model="newAnswerBody"  
                        class="form-control"
                        placeholder="Share your knowledge"
                        rows="5"
                        ></textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-success">submit your answer</button>
                    </div>
                </form>
                <p v-if="error" class="error mt-2">{{error}}</p>


            </div>
            <div v-else>
                <button
                class="btn btn-sm btn-success"
                @click="showForm = true"
                >Answer the Question
                </button>
            </div>
            <hr>
        </div>    
        <div class="container">
            <AnswerComponent 
                v-for="(answer,index) in answers"
                :answer="answer"
                :key="index"
            />

        </div>
    </div>
</template>



<script>
import { apiService } from "../common/api.service.js";
import AnswerComponent from "@/components/Answer.vue";
export default {
    name:"Question",
    props: {
        slug: {
            type:String,
            required: true
        }
    },
    components: {
        AnswerComponent
    },
    data() {
        return {
            question: {},
            answers: [],
            newAnswerBody: null,
            error: null,
            userHasAnswered: false,
            showForm: false


        }
    },
    methods: {
        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint)
                .then(data => {
                    this.question = data;
                    this.userHasAnswered = data.user_has_answered; 
                })
        },
        getQuestionAnswers() {
            let endpoint = `/api/questions/${this.slug}/answers/`;
            apiService(endpoint)
                .then(data => {
                    this.answers = data.results;
                })
        },
        onSubmit() {
            if (this.newAnswerBody) {
                let endpoint = `/api/questions/${this.slug}/answer/`;
                apiService(endpoint,"POST",{ body:this.newAnswerBody })
                    .then(data => {
                        this.answers.unshift(data)
                    })
                this.newAnswerBody = null;
                this.showForm = false
                this.userHasAnswered = true
                if (this.error) {
                    this.error = null;
                }

            } else {
                this.error = "you cant send an empty answer!";
            }

        },
    },
    created() {
        this.getQuestionData()
        this.getQuestionAnswers()

    }
}
</script>


<style  scoped>

.answer-added {
    font-weight: bold;
    color: green;
}

.error {
    font-weight: bold;
    color: red;
}

</style>