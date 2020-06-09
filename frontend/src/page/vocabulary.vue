<template>
    <div class="words_content">
        <head-top></head-top>
        <div class="words_menu">
            <button @click="words_list" value="cte4">4级单词</button>
            <button @click="words_list" value="cte6">6级单词</button>
        </div>
        <div class="views">
            <div class="view_style" v-for="item in words" v-bind:key="item.id">
                <div class="view_line">
                    <div class="view_en">{{item.en}}</div>
                        <div class="view_ch">
                            <span class="view_category">{{item.category}}</span>
                            <span>{{item.ch}}</span>
                        </div>
                </div>
            </div>
            <pagination v-if="words" pre-text="上一页" next-text="下一页" @pagefn='pagefn' :page=curpage :totalPage='endpage'></pagination>
        </div>
    </div>    
</template>

<script>
import { wordslist } from '../axios/axios'
import headTop from '../components/headTop'
import pagination from '../components/pagination'

export default {
    data(){
        return{
            words:'',
            curpage:1,
            endpage:'',
            type:''
        }
    },
    methods:{
        words_list(value){
            if(this.$store.state.userInfo.name==''){
                this.$message('请登入后在使用')
                return
            }
            this.type = value.target.value
            wordslist({type:this.type,page:this.curpage}).then((Response)=>{
                this.words = Response.data.results
                this.endpage = Math.ceil(Response.data.count/8)
            })
            this.curpage = 1
        },
        cur_words(curpage){
            wordslist({type:this.type,page:curpage}).then((Response)=>{
                this.words = Response.data.results
            })
        },
        pagefn(value){
            this.curpage = value.page
            this.cur_words(this.curpage)
        }
    },

    components:{
        headTop,
        pagination
    }
}
</script>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    outline: none;
}
.words_content{
    padding-top: 70px;
}
.words_menu{
    text-align: center;
}
.views{
    width: 1144px;
    margin:0 auto;
}
.view_style{
    width: 50%;
    display: inline-block;
    padding: 10px 10%;
    vertical-align: top;
}
.view_line{
    padding-top: 10px;
    border-top: .5px solid #dfe2eb;
}
.view_en{
    font-family: Helvetica;
    font-size: 18px;
    font-weight: 700;
    color: #333;
    flex-grow: 1;
}
.view_ch{
    font-size: 15px;
    color: #666;
    margin-top: 11px;
}
.view_category{
    margin-right: 10px;
    font-family: Roboto;
    font-style: italic;
}
</style>