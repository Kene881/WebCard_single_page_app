<template>
    <div class="w-full h-85 bg-green-100">
        <p class="text-center text-3xl font-semibold pt-10">Technologies</p>
        <div class="flex p-9 h-72 text-white">
            <div class="flex-1 flex-col bg-green-700 m-3 mx-14 rounded-md flex flex-wrap content-center justify-center">
                <img class="h-20 w-20" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/1184px-Vue.js_Logo_2.svg.png"/>
                <span class="text-center pt-3">Vuejs</span>
            </div>
    
            <div class="flex-1 flex-col bg-gray-500 m-3 mx-14 rounded-md flex flex-wrap content-center justify-center">
                <img class="h-20 w-20" src="https://static-00.iconduck.com/assets.00/fastapi-icon-512x512-a7ggfxfw.png"/>
                <span class="text-center pt-3">FastApi</span>
            </div>
    
            <div class="flex-1 flex-col bg-teal-800 m-3 mx-14 rounded-md flex flex-wrap content-center justify-center">
                <img class="h-20 w-20" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tailwind_CSS_Logo.svg/2048px-Tailwind_CSS_Logo.svg.png"/>
                <span class="text-center pt-3">Tailwind</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Technologies',
}
</script>