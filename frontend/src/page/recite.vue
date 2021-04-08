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
                        <div class="result_icon" style="display:inline-block">
                            <i class="el-icon-error" style="color:#f50808" v-if="results[item.en] === false"></i>
                            <i class="el-icon-success" style="color:#91d46f" v-if="results[item.en] === true"></i>
                        </div>
                        <div class="correct_word" v-if='results[item.en] == false' :class="{word_trun:disp}">
                            <span style="font-size:10.5pt">{{ item.ch }}</span>
                        </div>
                    </div>
                    <div class="words_ch" v-if="model.translate==='en'">
                        <div class="word_ch" :title="item.ch">{{ item.ch }}</div>
                        <input type="text" v-model.lazy="anwser[item.ch]" style="border-bottom: 1px solid gray;outline: none;"/>
                        <div class="result_icon" style="display:inline-block">
                            <i class="el-icon-error" style="color:#f50808" v-if="results[item.ch] === false"></i>
                            <i class="el-icon-success" style="color:#91d46f" v-if="results[item.ch] === true"></i>
                        </div>
                        <div class="correct_word" v-if='results[item.ch] == false' :class="{word_trun:disp}">
                            <span style="font-size:10.5pt">{{ item.en }}</span>
                        </div>
                    </div>
            </el-col>
        </el-row>
        <div class="result_menu">
            <div class="view_result" v-if="hidden" >
                <el-button :plain="true" @click=view_result>查看结果</el-button>
            </div>
            <div class="after_result" v-if="show">
                <el-button :plain="true" @click=change_word>换一批</el-button>
                <el-button :plain="true"  @click=correct_word>查看正确的单词</el-button>
                <el-button :plain="true"  @click=again>在试一次</el-button>
                <el-button :plain="true"  @click=save_word>保存错词</el-button>
            </div>
        </div>
    </div>
</div>    
</template>

<script>
import headTop from '../components/headTop'
import {generate,useraw,next,userlearned} from '../axios/axios'

export default {
    data(){
        return {
            words: null,
            model: null,
            anwser:{},
            results:{},
            hidden: true,
            show: false,
            disp: false,
            next:null,
        }
    },
 
    created(){
        this.getwords()
    },


    methods:{
        getwords(){
            this.model = this.$route.params
            generate({level:this.model.level,num:this.model.num,model:this.model.model}).then((response)=>{            
                this.words = response.data.results
                this.next = response.data.next
            })
        },

        view_result(){
            let k_word = Object.keys(this.anwser)
            if(k_word.length != this.words.length){
                this.$message("请填写完所有单词(不会随便填)")
                return
            }
            let v_word = Object.values(this.anwser)
            for(let i in v_word){
                if(v_word[i] === ""){
                    this.$message("请填写完所有单词(不会随便填)")
                    return
                }
            if(this.model.translate === 'ch'){
                for(let i in v_word){
                    for(let j in this.words){
                        if(k_word[i] === this.words[j].en){
                            if(this.words[j].ch.match(v_word[i])){
                            this.results[k_word[i]] = true
                            }else{
                            this.results[k_word[i]] = false
                            }
                    }
                }
                }
            }
            if(this.model.translate === 'en'){
                for(let i in v_word){
                    for(let j in this.words){
                        if(k_word[i] === this.words[j].ch){
                            if(this.words[j].en.match(v_word[i])){
                            this.results[k_word[i]] = true
                            }else{
                            this.results[k_word[i]] = false
                        }
                    }
                }
                }
            }
            }
            this.hidden = false;
            this.show = true;
        },

        change_word(){
            let token_str = 'token'+this.$store.state.userInfo.token
            let info ={
                headers:{
                    'authorization': token_str.replace('token','JWT ')
                }
            }
            this.model = this.$route.params
            if(this.$store.state.userInfo.name ==''){
                this.$message('你还未登入，请登入后使用')
                return
            }
            if(this.$store.state.userInfo.name!=''){
                for(let i in this.words){
                    userlearned({cte4:this.words[i]['Id']},info).then((Response)=>{
                        console.assert(Response.data)
                    })
                }
            this.$notify({
                title: '成功',
                message: '保存成功',
                type: 'success'
            })                
            }
            next(this.next).then((response)=>{
                this.words = response.data.results
                this.next = response.data.next
            })        
            this.anwser = {}
            this.results = {}
            this.hidden = true
            this.show = false
            this.disp = false
        },

        correct_word(){
            this.disp = true
        },

        save_word(){
            let token_str = 'token'+this.$store.state.userInfo.token
            let info ={
                headers:{
                'authorization': token_str.replace('token','JWT ')
                }
            }   
            if(this.$store.state.userInfo.name ==''){
                this.$message('你还未登入，请登入后使用')
                return
            }
            for(let i in this.results){
                if(this.results[i] == false){
                    for(let j in this.words){
                        if(this.words[j]['ch']==i || this.words[j]['en']==i){
                            useraw({save_cte4_words:this.words[j]['Id']},info).then((Response)=>{
                                console.assert(Response.data)
                            })
                        }
                    }
                }
            }
            this.$notify({
                title: '成功',
                message: '保存成功',
                type: 'success'
            })
        },

        again(){
            var i = 0
            var random_word = []
            var word_len = this.words.length
            while(i < word_len){
                let random_num = Math.round(Math.random()*(this.words.length-1))
                random_word.push(this.words[random_num])
                this.words.splice(random_num, 1)
                i++
            }
            this.anwser = {}
            this.results = {}
            this.hidden = true
            this.show = false
            this.disp = false
            this.words = random_word
            return
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

.word_ch{
    display: inline-block;
    padding-right: 10px;
    font-size: 12px;
    padding: 5px;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    width: 100px;
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
    display: none;
    margin-top: 10px;
}
.word_trun {
    display: block;
}

.el-message__icon{
    color: red !important;
}

.el-message__content{
    color:red !important;
}

</style>