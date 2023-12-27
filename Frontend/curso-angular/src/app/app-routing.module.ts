import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FirstComponentComponent } from './components/first-component/first-component.component';
import { ListRenderComponent } from './components/list-render/list-render.component';
import { IfRenderComponent } from './components/if-render/if-render.component';
import { HomeComponent } from './pages/home/home.component';
import { CadastroTutor1Component } from './pages/cadastro-tutor1/cadastro-tutor1.component';
import { CadastroFotoComponent } from './components/cadastro-foto/cadastro-foto.component';
import { ListarCuidadoresComponent } from './pages/listar-cuidadores/listar-cuidadores.component';
import { ListarcuidadorComponent } from './pages/listarcuidador/listarcuidador.component';
import { BuscarCuidadorComponent } from './pages/buscar-cuidador/buscar-cuidador.component';

const routes: Routes = [
    {path: '',component: FirstComponentComponent},
    {path: 'list', component: ListRenderComponent},
    {path: 'ifrender', component: IfRenderComponent},
    {path: 'home', component: HomeComponent},
    {path: 'cadastrar', component: CadastroTutor1Component},
    {path: 'cadastro-foto', component: CadastroFotoComponent},
    {path: 'cuidadores', component: ListarCuidadoresComponent},
    {path: 'buscar-cuidador', component: BuscarCuidadorComponent}
];

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
