import { Injectable } from '@angular/core';
import { Cuidador } from '../Cuidador';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CuidadorService {

  url = 'http://127.0.0.1:8000/api/v1/';

  constructor(private http: HttpClient) { }

  getCuidadors(): Observable<Cuidador[]> {
    return this.http.get<Cuidador[]>(this.url + 'cuidadores/');
  }


}
