<template>
    <div class="content">
        <head-top></head-top>
        <div>
            <button @click="cte4">4级单词</button>
            <button @click="cte6">6级单词</button>
        </div>
        <div class="views">
            <div v-if="check==='cte4'">
                <div class="view_style" v-for="item in cte4_words" v-bind:key="item.id">
                    <div class="view_line">
                        <div class="view_en">{{item.en}}</div>
                        <div class="view_ch">
                            <span class="view_category">{{item.category}}</span>
                            <span>{{item.ch}}</span>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="check==='cte6'">
                <div class= "view_style" v-for="item in cte6_words" v-bind:key="item.id">
                    <div class="view_line">
                        <div class="view_en">{{item.en}}</div>
                        <div class="view_ch">
                            <span class="view_category">{{item.category}}</span>
                            <span>{{item.ch}}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>

<script>
import { wordslist } from '../axios/axios'
import headTop from '../components/headTop'

export default {
    data(){
        return{
            cte4_words:'',
            cte6_words:'',
            check:''
        }
    },
    methods:{
        cte4(){
            if(this.$store.state.userInfo.name ==''){
                this.$message('你还未登入，请登入后使用')
                return
            }
            if(this.cte4_words == ''){
                wordslist({type:'cte4'}).then((Response)=>{
                    this.cte4_words = Response.data
                })
            }
            this.check = 'cte4'
        },
        cte6(){
            if(this.$store.state.userInfo.name ==''){
                this.$message('你还未登入，请登入后使用')
                return
            }
            if(this.cte6_words == ''){
                wordslist({type:'cte6'}).then((Response)=>{
                    this.cte6_words = Response.data
            })
            }
            this.check = 'cte6'
        }
    },
    components:{
        headTop,
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