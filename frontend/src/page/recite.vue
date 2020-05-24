<template>
<div class="recite">
    <head-top></head-top>
    <div class="padding"></div>
    <div class="recite_word">
        <el-row>
            <el-col :span='6' v-for="item in words" v-bind:key ="item.id" class="word_style">
                    <div class="words_en" v-if="model.translate==='ch'">
                        <div class="word_en">{{ item.en }} </div>
                        <input type="text" v-model.lazy="anwser[item.en]" style="border-bottom: 1px solid gray;outline: none;"/>
                        <div class="result_icon">
                            <div v-if="results[item.en] === false">
                                <i class="el-icon-error" style="color:#f50808"></i>
                            </div>
                        </div>
                        <div class="correct_word" v-if='results[item.en] == false'>
                            <span style="font-size:10.5pt">{{ item.ch }}</span>
                        </div>
                    </div>
                    <div class="words_ch" v-if="model.translate==='en'">{{ item.ch }}</div>
            </el-col>
        </el-row>
        <div class="result_menu">
            <div class="view_result" v-if="hidden" >
                <button @click=view_result>查看结果</button>
            </div>
            <div class="after_result" v-if="show">
                <button @click=change_word>换一批</button>
                <button @click=correct_word>查看正确的单词</button>
                <button @click=save_word>保存错词</button>
            </div>
        </div>
    </div>
</div>    
</template>

<script>
import headTop from '../components/headTop'
import {generate} from '../axios/axios'

export default {
    data(){
        return {
            words: null,
            model: null,
            anwser:{},
            results:{},
            hidden: true,
            show: false,
        }
    },
 
    created(){
        this.getwords()
    },


    methods:{
        getwords(){
            this.model = this.$route.params
            console.log(this.$route.params)
            generate({level:this.model.level,num:this.model.num}).then((response)=>{
                this.words = response.data
                console.log(response.data)
            })
        },

        view_result(){
            let en_word = Object.keys(this.anwser)
            if(en_word.length != this.words.length){
                alert('请填写完所有单词')
                return
            }
            let ch_word = Object.values(this.anwser)
            for(let i in ch_word){
                if(ch_word[i] === ""){
                    alert("请填写完所有单词")
                    return
                }
                for(let j in this.words){
                    if(en_word[i] === this.words[j].en){
                        if(this.words[j].ch.match(ch_word[i])){
                            this.results[ch_word[i]] = true
                        }else{
                            this.results[en_word[i]] = false
                        }
                    }
                }
            } 
            this.hidden = false;
            this.show = true;
        },

        change_word(){

        },

        correct_word(){

        },

        save_word(){
              
        }

    },
    components:{
        headTop
    }

}
</script>

<style>
.padding{
    height: 70px;
}

.recite_word{
    padding: 20px;
    margin-top: 30px;
}

.word_style{
    color:#666;
    font-family: Helvetica;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 50px;
}

.word_en{
    display: inline-block;
    padding-right: 10px;
}
.words_en{
    padding-left: 10px;
}

.result_menu{
    margin-top: 50px;
    text-align: center;
}

button{
    padding: 10px;
    margin: 10px;
}
.correct_word{
    font-size: 0px;
    padding: 5px;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    width: auto;
    display: block;
}

</style>