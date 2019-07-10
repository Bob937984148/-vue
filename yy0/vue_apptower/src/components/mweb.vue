<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.14.1/lodash.min.js"></script>
<template>
<div id="flip-list-demo" class="demo">
  <button @click="shuffle">
    Shuffle
  </button>
  <transition-group name="cell" tag="div" class="container">
    <div v-for="cell in cells" :key="cell.id" class="cell">
      {{ cell.number }}
    </div>
  </transition-group>
</div>
</template>
<script>
export default {
    data(){
        return {
        cells: Array.apply(null, { length: 81 })
    	  .map(function (_, index) { 
      	return {
        	id: index,
        	number: index % 9 + 1
        }
      })
  }
},
  methods: {
    shuffle: function () {
      this.items = (this.items).sort(function(a,b){
          return b-a;
      });

    },

  }
}
</script>
<style>
.container {
  display: flex;
  flex-wrap: wrap;
  width: 238px;
  margin-top: 10px;
}
.cell {
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 25px;
  height: 25px;
  border: 1px solid #aaa;
  margin-right: -1px;
  margin-bottom: -1px;
}
.cell-move {
  transition: transform 1s;
}
</style>

