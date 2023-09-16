<template>
  <div class="card">
    <!-- Card header -->
    <div class="card-header py-3 d-flex align-items-center border-bottom">
        <div class="d-flex align-items-center">
          <!-- Surtitle -->
          <!-- <h6 class="surtitle">5/23 projects</h6> -->
          <!-- Title -->
          <h5 class="text-capitalize">Nevera Biologicos</h5>
        </div>
        <div class="text-end ms-auto">
          <a href="#!" class="mb-0 btn btn-xs bg-neutral">
            <i class="fas fa-cog "></i> 
            Config
          </a>
        </div>
    </div>
    <!-- Card body -->
    <div class="card-body card-body-indicator">
      <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab dolorum natus architecto aliquam, labore accusamus error ut dolorem nobis quo odio? Tenetur pariatur ad perspiciatis culpa, mollitia ipsa placeat iusto?</p> -->
      <div class="push-indicator push-indicator--green-light">
        <div class="push-in-indicator">
          <p class="display">
            <span id="temperatura_entero" class="temp_entero"> 20</span>
            <span id="temperatura_decimal" class="temp_decimal">.5</span>
            <span class="temp_grados">&deg;</span>
          </p>
        </div>
      </div>
      <p class="mt-3 mb-0 text-center" >31-12-12 00:00:00</p>
    </div>
  </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.push-indicator {
  position: relative;
  margin: 0 auto;
  // border:1px solid red;
  border-radius: 50%;
  padding: 20px;
  width: 200px;
  height: 200px;
  // text-align: center;
}

.push-indicator--blue-light {
  background: linear-gradient(
    360deg,
    #0c9bec 0%,
    rgba(12, 155, 236, 0.42) 48.97%,
    rgba(12, 155, 236, 0.916667) 100%
  );
  box-shadow: 0px 4px 4px rgba(6, 151, 177, 0.46);
}

.push-indicator--green-light {
  background: linear-gradient(
    360deg,
    #06b10d 0%,
    rgba(6, 145, 53, 0.42) 48.97%,
    rgba(6, 177, 13, 0.916667) 100%
  );
  box-shadow: 0px 4px 4px rgba(6, 177, 13, 0.46);
}

.push-indicator--red-light {
  background: linear-gradient(
    360deg,
    #c91d12 0%,
    rgba(201, 29, 18, 0.42) 48.97%,
    rgba(201, 29, 18, 0.916667) 100%
  );
  box-shadow: 0px 4px 4px rgba(201, 29, 18, 0.46);
}

.push-in-indicator {
  border-radius: 50%;
  padding: 4px;
  // width: 100px;
  height: 100%;
  // margin: 0 auto;
  // border:1px solid red;
  background: #fff9f9;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.display {
  display: flex;
  border-radius: 50%;
  // border:1px solid red;
  height: 100%;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 24px;
  line-height: 33px;
  color: #a29f9f;
}
</style>
