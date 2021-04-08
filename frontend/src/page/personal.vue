<template>
    <div class="personal_page">
        <head-top></head-top>
        <div class="personal_content">
            <div class="personal_cc">
                <div class="personal_info">
                    <div class="user_avater">
                        <div>
                            <img class="users_avatar" src='../static/svg/avatar.jpg'>
                        </div>
                        <div style="margin-left:14px">
                            <p style="font-family: PingFangTC-Medium;font-size: 17px;font-weight: 500;color: #333;">{{ userInfo.name }}</p>
                        </div>
                        <div class="learn_summary">
                            <div>已默<span class="words_num">{{ user_info.total_learned_num }}</span>单词</div>
                            <div>保存<span class='wrong_words_num'>{{ user_info.total_wrong_words }}</span>错词</div>
                        </div>
                    </div>
                </div>
                <div class="show_words" v-if='html_words'>
                    <div class="" v-for="item in show_words" v-bind:key="item.id">
                        <div class="">
                            <div class="w_view_en">{{item.en}}</div>
                            <div class="w_view_ch">
                                <span class="w_view_category">{{item.category}}</span>
                                <span>{{item.ch}}</span>
                            </div>
                        </div>
                    </div>
                    <pagination v-if="get_words" pre-text="上一页" next-text="下一页" @pagefn='pagefn' :page=curpage :totalPage='endpage'></pagination>
                </div>
                <div class="current_learn">
                    <el-tabs v-model="activeName" @tab-click="get_words_num">
                        <el-tab-pane label="CTE4" name="first"></el-tab-pane>
                        <el-tab-pane label="CTE6" name="second"></el-tab-pane>
                        <el-tab-pane label="TOEFL" name="third"></el-tab-pane>
                        <el-tab-pane label="IELTS" name="fourth"></el-tab-pane>
                    </el-tabs>
                    <div class="learn_detail">
                        <ul class="words_style">
                            <li>总数 :<span style="color: rgba(27, 255, 0, 0.71);">{{ type_wordsnum }}</span>
                            </li>
                            <li>已默 :<span style="color:#00bcd4">{{ type_user_words.learned }}</span>
                            </li>
                            <li>错词 :<span style="color:#e91e1e;">{{ type_user_words.wrong }}</span>
                            </li>
                            <li>近期 :<span style="color:#f3cc0c">{{ cur_num_words }}</span>
                            </li>
                        </ul>
                        <ul class="icon-view">
                            <li><span class="el-icon-view viewwords"  @click="f_get_words('total')"></span></li>
                            <li><span class="el-icon-view viewwords" :class="[this.view_model==='learned'?'words_learned':'']" @click="f_get_words('learned')"></span></li>
                            <li><span class="el-icon-view viewwords" :class="[this.view_model==='wrongwords'?'words_wrongwords':'']" @click="f_get_words('wrongwords')"></span></li>
                            <li><span class="el-icon-view viewwords" :class="[this.view_model==='current'?'words_current':'']" @click="f_get_words('current')"></span></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import headTop from '../components/headTop'
import { mapGetters } from 'vuex'
import { userinfo,wordsdetail,learnedDetail,usercurlearned } from '../axios/axios' 
import pagination from '../components/pagination'

export default{

    data(){
        return{
            activeName:'first',
            type_wordsnum:'',
            type_user_words:'',
            user_info:'',
            get_words:[],
            show_words:'',
            curpage:1,
            endpage:'',
            html_words:false,
            view_model:'',
            type:'cte4',
            cur_num_words:'',
        };
    },

    computed:{
        ...mapGetters({
            userInfo:'userInfo',
            wordsnum:'wordsnum',
        })
    },
    components:{
        headTop,
        pagination
    },

    methods:{
        get_words_num(tab){
            this.type = tab.label.toLowerCase() 
            this.type_wordsnum = this.$store.state.wordsnum[this.type]
            if (this.type=='cte4'){
                this.view_model=''
                this.html_words=false
                this.get_words = []
                this.show_words = ''
                this.endpage = ''                
                this.type_user_words['learned'] = this.user_info.learned_cte4_num
                this.type_user_words['wrong'] = this.user_info.wrong_4words_num
                this.type_user_words['current'] = this.cur_num_words
                }
            if (this.type=='cte6'){
                this.view_model=''
                this.html_words=false
                this.get_words = []
                this.show_words = ''
                this.endpage = ''
                this.type_user_words['learned'] = this.user_info.learned_cte6_num
                this.type_user_words['wrong'] = this.user_info.wrong_6words_num
                this.type_user_words['current'] = this.cur_num_words        
            }
        },
        get_user_info(){
            this.type_wordsnum = this.$store.state.wordsnum.cte4
            let token_str = 'token'+this.$store.state.userInfo.token
            let info ={
                headers:{
                'authorization': token_str.replace('token','JWT ')
                }
            }
            userinfo(info).then((Response)=>{
                this.user_info = Response.data['0']
                this.type_user_words = {
                learned:Response.data['0'].learned_cte4_num,
                wrong:Response.data['0'].wrong_4words_num,
            }
            })
            usercurlearned(info).then((Response)=>{
                this.cur_num_words = Response.data.length
            })
            
        },
        f_get_words(model){
            if(this.view_model != ''){
                if(this.view_model==model){
                    this.view_model=''
                    this.html_words=false
                    this.get_words=[]
                    this.show_words=''
                }
                else{
                    this.view_model=model
                    this.get_words=[]
                    this.show_words=''
                }
            }
            else if(this.view_model==''){
                if(model=='learned'){
                    this.html_words=true
                    this.view_model=model
                }
                if(model=='wrongwords'){
                    this.html_words=true
                    this.view_model=model
                }
                if(model=='current'){
                    this.html_words=true
                    this.view_model=model
                }
                if(model=='total'){
                    this.$router.push({name:'vocabulary'})
                }          
            } 
        },
        level_cur_words(curpage){
            if(this.get_words.length<=15){
                this.show_words=this.get_words.slice(0,this.get_words.length)
            }
            else if(curpage==this.endpage){
                var lastpage_num = this.get_words.length%15
                var last_start = this.get_words.length-lastpage_num
                this.show_words = this.get_words.slice(last_start, this.get_words.length)
            }
            else{
                var end = curpage*15
                var start = end-15
                this.show_words = this.get_words.slice(start,end)
            }
        },
        pagefn(value,){
            this.curpage = value.page
            this.level_cur_words(this.curpage)
        }


    },
    created(){
        this.get_user_info()
    },
    watch:{
        view_model(val){
            var that = this
            let token_str = 'token'+this.$store.state.userInfo.token
            let info ={
                headers:{
                'authorization': token_str.replace('token','JWT ')
                }
            }
            var type_proc = function(type, wrong_words){
                if(val=='learned'){
                    learnedDetail(info).then((Response)=>{
                        for(let i of Response.data){
                            that.get_words.push(i[type])
                        }
                    })
                    setTimeout(()=>{
                        that.endpage=Math.ceil(that.get_words.length/15)
                        that.pagefn({'page':1})
                    },100)
                }                        
                if(val=='wrongwords'){
                    wordsdetail(info).then((Response)=>{
                        for(let i of Response.data){
                            that.get_words.push(i[wrong_words])
                        }
                    })
                    setTimeout(()=>{
                        that.endpage=Math.ceil(that.get_words.length/15)
                        that.pagefn({'page':1})
                    },100)
                }
                if(val=='current'){
                    usercurlearned(info).then((Response)=>{
                        for(let i of Response.data){
                            that.get_words.push(i[type])
                        }
                    })
                    setTimeout(()=>{
                        that.endpage=Math.ceil(that.get_words.length/15)
                        that.pagefn({'page':1})
                    },100)                    
                }
            }
            if(this.type=='cte4'){
                type_proc('cte4','save_cte4_words')
            }   
        }
    },
}
</script>
<style>
.personal_content{
    padding-top: 100px;
}
.personal_cc{
    width: 1000px;
    margin: auto;
}
.personal_info{
    margin-bottom: 15px;
}
.user_avater{
    margin-left: 100px;
    display: flex;
    align-items: center;
}
.users_avatar{
    border-radius: 50%;
    width: 60px;
	height: 60px;
	border-style: none;
}
.current_learn{
    width: 200px;
    float: right;
}
.learn_detail{
    display: flex;
}
.learn_summary{
    font-family: PingFangTC-Regular;
    font-size: 18px;
    color: #666;
    position: fixed;
    right: 400px;
}
.words_num{
    font-family: Impact;
    color: #27b38f;
    padding: 0 8px;
}
.wrong_words_num{
    font-family: Impact;
    color: #f56c6c;
    padding: 0 8px;
}
.words_style{
 font-family: PingFangSC-Light;
    font-size: 14px;
    line-height: 24px;
    color: #666;
    padding-left: 20px;
}
.words_style > li{
    margin-bottom: 3px;
}
.words_style > li > span{
    margin-left: 7px;
}
.viewwords{
    cursor:pointer;
    font-size: 14px;
}
.icon-view{
    line-height:24px;
    margin-left: auto;
}
.icon-view > li{
    padding-bottom: 3px;
}
.words_learned{
    color:rgb(0, 188, 212);
}
.words_wrongwords{
    color:rgb(233, 30, 30);
}
.words_current{
    color:rgb(243, 204, 12);
}
.show_words{
    width: 700px;
    display: inline;
    float: left;
}
.w_view_en{
    font-family: Helvetica;
    font-size: 14px;
    font-weight: 700;
    color: #333;
    display: inline;
}
.w_view_ch{
    font-size: 12px;
    color: #666;
    float:right;   
}
.w_view_category{
    margin-right: 10px;
    font-family: Roboto;
    font-style: italic;
}
</style>