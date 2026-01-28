import { User, Patient, Appointment } from '@hospital/types';

export interface ApiClientConfig {
  baseUrl: string;
  headers?: Record<string, string>;
}

export class ApiClient {
  private baseUrl: string;
  private headers: Record<string, string>;

  constructor(config: ApiClientConfig) {
    this.baseUrl = config.baseUrl;
    this.headers = config.headers || {};
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...this.headers,
        ...options.headers,
      },
    });

    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }

    return response.json();
  }

  // Health check
  async healthCheck(): Promise<{ status: string; timestamp: string }> {
    return this.request('/health');
  }

  // User endpoints (placeholder)
  async getUsers(): Promise<User[]> {
    return this.request('/api/users');
  }

  async getUser(id: string): Promise<User> {
    return this.request(`/api/users/${id}`);
  }

  // Patient endpoints (placeholder)
  async getPatients(): Promise<Patient[]> {
    return this.request('/api/patients');
  }

  async getPatient(id: string): Promise<Patient> {
    return this.request(`/api/patients/${id}`);
  }

  // Appointment endpoints (placeholder)
  async getAppointments(): Promise<Appointment[]> {
    return this.request('/api/appointments');
  }

  async getAppointment(id: string): Promise<Appointment> {
    return this.request(`/api/appointments/${id}`);
  }
}

export default ApiClient;
