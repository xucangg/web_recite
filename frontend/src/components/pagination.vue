<template>
    <div>
        <div class="index_tableFoot">
            <div class="index_pagination">
                <ul class="index_pageContainer">
                    <li v-for="page in pages" :key="page.id" @click='pageCallback(page.page)' :class="[page.active?'index_active':'',page.banclick?'ban':'',page.index_nomore?'index_nomore':'']">{{page.text}}</li>
                </ul>
             </div>
        </div>
    </div>
</template>



<script>
export default {
    props:{
        preText:{
            type:String,
            default:'上一页'
            },
        nextText:{
            type:String,
            default:'下一页'
            },
        page:[String,Number],
        totalPage:[String, Number]
    },
    
    methods:{
        pagina(curpage,endpage){
            var pages = []
            /*当总页数为1当前页数为1时返回分页*/
            if(curpage<=1 && endpage===1) {pages.push({text:endpage,active:true});return pages} 
            var d = 1
            /*当前页不等于1时，添加上一页可以点击页*/
            curpage===1?pages.push({page:1,text:this.preText,index_nomore:true}):pages.push({page:curpage-1,text:this.preText})
            /*当前页面大于4，添加分页内容，第一页标签页，和省略号*/
            if(curpage>4) d = curpage-2,pages.push({page:1,text:1}),pages.push({text:'...',banclick:true})
            /*添加当前页的前两页可点击分页*/
            if(endpage-curpage>=0 && curpage>=1) for(; d<curpage;d++) pages.push({page:d,text:d})
            /*添加当前页*/
            pages.push({page:curpage,text:curpage,active:true})
            var e = 1
            /*当前页到末页还剩3页或小于3页，添加当前页到末页的可点击页*/
            if(endpage-curpage<=3){e = curpage+1;for(;e<=endpage;e++) pages.push({page:e,text:e})}
            /*当前页到末页大于3页，添加当前页后两页，省略号和末页*/
            if(endpage-curpage>3){
                e = curpage+1;
                for(;e<=curpage+2;e++){pages.push({page:e,text:e})}
                pages.push({text:'...',banclick:true})
                pages.push({page:endpage,text:endpage})
                }
            /*当前页选择到末页时，添加下一页不可点样式，为选择到末页，添加下一页可点击页*/
            curpage-endpage===0?pages.push({page:endpage,text:this.nextText,index_nomore:true}):pages.push({page:curpage+1,text:this.nextText})
            return pages
        },
        pageCallback:function(page){
            this.$emit('pagefn',{page:page})
      }
    },

    computed:{
        pages:function(){
            return this.pagina(parseInt(this.page),this.totalPage)
        }
    }
}
</script>


<style>
.index_tableFoot{
    margin-top: 50px;
    padding: 0 10%;
}
.index_pageContainer > li{
    list-style: none;
    float: left;
    padding: 0 8px;
    cursor: pointer;
    border: 1px solid #ccc;
    height: 28px;
    line-height: 28px;
    margin-right: 8px;
}
.index_nomore{
    color: #b5b5b5!important;
    cursor: not-allowed!important;
}
.index_active{
    color: #fff!important;
    background: #28bea0;
    border-radius: 1px;
}
.ban{
    pointer-events:none;
}
</style>