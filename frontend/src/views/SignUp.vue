<template>
  <div class="signup">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign Up</h1>
      </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <form action="">

                        <div class="field">
                            <label>Email</label>
                            <div class="control">
                                <input type="email" class="input">
                            </div>
                        </div>

                        <div class="field">
                            <label>Password</label>
                            <div class="control">
                                <input type="password" class="input">
                            </div>
                        </div>

                        <div class="field">
                            <label>Repeat Password</label>
                            <div class="control">
                                <input type="password" class="input">
                            </div>
                        </div>

                        <div class="field">
                            <div class="control">
                                <button class="button is-dark is-info">Sign Up</button>
                            </div>
                        </div>
                        
                    </form>
                    <hr>
                    Or <RouterLink to ='/log-in'>Click to log in!</RouterLink>
                </div>
            </div>
        </div>
    </section>

  </div>
</template>
