import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { FirstComponentComponent } from './components/first-component/first-component.component';
import { ParentDataComponent } from './components/parent-data/parent-data.component';
import { DirectivesComponent } from './components/directives/directives.component';
import { IfRenderComponent } from './components/if-render/if-render.component';
import { EventosComponent } from './components/eventos/eventos.component';
import { EmitterComponent } from './components/emitter/emitter.component';
import { ChangeNumberComponent } from './components/change-number/change-number.component';
import { ListRenderComponent } from './components/list-render/list-render.component';
import { PipesComponent } from './components/pipes/pipes.component';
import { TwoWayBindingComponent } from './components/two-way-binding/two-way-binding.component';
import { HomeComponent } from './pages/home/home.component';
import { CadastroTutor1Component } from './pages/cadastro-tutor1/cadastro-tutor1.component';
import { CadastroFotoComponent } from './components/cadastro-foto/cadastro-foto.component';
<<<<<<< HEAD
import { ListarCuidadoresComponent } from './pages/listar-cuidadores/listar-cuidadores.component';
import { ListarcuidadorComponent } from './pages/listarcuidador/listarcuidador.component';
import { CardCuidadoresComponent } from './components/card-cuidadores/card-cuidadores.component';
import { BuscarCuidadorComponent } from './pages/buscar-cuidador/buscar-cuidador.component';

=======
import { ListarcuidadorComponent } from './components/listarcuidador/listarcuidador.component';
>>>>>>> 9fc74eeffb0b0f50649d41943c2720a3f24d7d30

@NgModule({
  declarations: [
    AppComponent,
    FirstComponentComponent,
    ParentDataComponent,
    DirectivesComponent,
    IfRenderComponent,
    EventosComponent,
    EmitterComponent,
    ChangeNumberComponent,
    ListRenderComponent,
    PipesComponent,
    TwoWayBindingComponent,
    HomeComponent,
    CadastroTutor1Component,
    CadastroFotoComponent,
<<<<<<< HEAD
    ListarCuidadoresComponent,
    ListarcuidadorComponent,
    CardCuidadoresComponent,
    BuscarCuidadorComponent,
    
=======
    ListarcuidadorComponent
>>>>>>> 9fc74eeffb0b0f50649d41943c2720a3f24d7d30
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
