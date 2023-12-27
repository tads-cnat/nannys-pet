import { Injectable } from '@angular/core';
import { Cuidador } from '../Cuidador';
import { Observable } from 'rxjs';
<<<<<<< HEAD
import { HttpClient,HttpParams } from '@angular/common/http';
import { Caracteristicas } from '../Caracteristicas';
=======
import { HttpClient } from '@angular/common/http';
>>>>>>> 9fc74eeffb0b0f50649d41943c2720a3f24d7d30

@Injectable({
  providedIn: 'root'
})
export class CuidadorService {

  url = 'http://127.0.0.1:8000/api/v1/';

  constructor(private http: HttpClient) { }

  getCuidadors(): Observable<Cuidador[]> {
    return this.http.get<Cuidador[]>(this.url + 'cuidadores/');
  }

<<<<<<< HEAD
  getCaracteristicasDoCuidador(cuidadorId: number): Observable<Caracteristicas> {
    const url = `${this.url}${cuidadorId}/caracteristicas`;
    return this.http.get<Caracteristicas>(url);
  }

  getCuidadoresFiltrados(filtros: any): Observable<Cuidador[]> {
    const url = `${this.url}cuidadores-filtrados/`;

    // Converta os filtros em HttpParams
    let params = new HttpParams();
    for (const key in filtros) {
      if (filtros.hasOwnProperty(key)) {
        params = params.set(key, filtros[key]);
      }
    }

    // Passe os parâmetros como parte da solicitação
    return this.http.get<Cuidador[]>(url, { params: params });
  }
}


=======

}
>>>>>>> 9fc74eeffb0b0f50649d41943c2720a3f24d7d30
