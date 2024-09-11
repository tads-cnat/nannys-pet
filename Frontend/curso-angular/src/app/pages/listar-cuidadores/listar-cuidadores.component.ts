import { Component, OnInit } from '@angular/core';
import { Cuidador } from '../../Cuidador';
import { CuidadorService } from '../../services/cuidador.service';

@Component({
  selector: 'app-listar-cuidadores',
  templateUrl: './listar-cuidadores.component.html',
  styleUrls: ['./listar-cuidadores.component.css'] // Corrigido de "styleUrl" para "styleUrls"
})
export class ListarCuidadoresComponent implements OnInit {
  cuidadors: Cuidador[] = [];
  filteredCuidadores: Cuidador[] = [];
  searchTerm: string = ''; // Termo de pesquisa

  constructor(private service: CuidadorService) {}

  ngOnInit() {
    // Busque os cuidadores e inicie a lista filtrada
    this.service.getCuidadors().subscribe(data => {
      this.cuidadors = data;
      this.filteredCuidadores = data; // Inicialmente, todos os cuidadores são exibidos
    });
  }

  // Método de filtro para buscar por cidade
  filterCuidadores() {
    const searchLower = this.searchTerm.toLowerCase(); // Para busca case-insensitive
    this.filteredCuidadores = this.cuidadors.filter(cuidador => 
      cuidador.localidade.toLowerCase().includes(searchLower)
    );
  }
}
