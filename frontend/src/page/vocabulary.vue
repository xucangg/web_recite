<template>
    <div>
        <button @click="cte4">4级单词</button>
        <button @click="cte6">6级单词</button>
    </div>    
</template>

<script>
import { wordslist } from '../axios/axios'

export default {
    data(){
        return{
            cte4_words:'',
            cte6_words:'',
        }
    },
    methods:{
        cte4(){
            wordslist({type:'cte4'}).then((Response)=>{
                this.cte4_words = Response.data
                console.log(Response)
                console.log(this.cte4_words)
            })
        },
        cte6(){
            wordslist({type:'cte6'}).then((Response)=>{
                this.cte6_words = Response.data
            })
        }
    }
}
</script>