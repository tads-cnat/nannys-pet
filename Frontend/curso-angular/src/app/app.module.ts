import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { CadastroTutor1Component } from './pages/cadastro-tutor1/cadastro-tutor1.component';
import { ListarCuidadoresComponent } from './pages/listar-cuidadores/listar-cuidadores.component';
import { CardCuidadoresComponent } from './components/card-cuidadores/card-cuidadores.component';
import { BuscarCuidadorComponent } from './pages/buscar-cuidador/buscar-cuidador.component';
import { CadastroCuidador1Component } from './pages/cadastro-cuidador1/cadastro-cuidador1.component';
import { LoginComponent } from './components/login/login.component';
import { AuthGuard } from './guards/auth.guard';
import { AuthService } from './services/auth.service';
import { CadastroUsuarioComponent } from './pages/cadastro-usuario/cadastro-usuario.component';
import { AuthInterceptor } from './services/auth.interceptor';
// import { HomeLogadoComponent } from './pages/home-logado/home-logado.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CadastroTutor1Component,
    ListarCuidadoresComponent,
    CardCuidadoresComponent,
    BuscarCuidadorComponent,
    CadastroCuidador1Component,
    LoginComponent,
    CadastroUsuarioComponent,
    // HomeLogadoComponent,
  ],


  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule
  ],


  providers: [
    AuthGuard,
    AuthService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],


  bootstrap: [AppComponent]
})
export class AppModule { }
