import { Button } from '@hospital/ui';

function App() {
  const handleClick = () => {
    alert('Welcome to Hospital Management System!');
  };

  return (
    <div style={{ 
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      fontFamily: 'system-ui, -apple-system, sans-serif'
    }}>
      <div style={{
        backgroundColor: 'white',
        borderRadius: '16px',
        padding: '48px',
        boxShadow: '0 20px 60px rgba(0,0,0,0.3)',
        maxWidth: '600px',
        textAlign: 'center'
      }}>
        <h1 style={{ 
          fontSize: '48px', 
          marginBottom: '16px',
          color: '#1a202c',
          fontWeight: 'bold'
        }}>
          🏥 Hospital Management System
        </h1>
        <p style={{ 
          fontSize: '20px', 
          marginBottom: '32px',
          color: '#4a5568',
          lineHeight: '1.6'
        }}>
          A modern, full-stack monorepo solution for healthcare management
        </p>
        <div style={{ display: 'flex', gap: '12px', justifyContent: 'center' }}>
          <Button variant="primary" onClick={handleClick}>
            Get Started
          </Button>
          <Button variant="secondary" onClick={() => window.open('http://localhost:3001/health', '_blank')}>
            Check API Status
          </Button>
        </div>
        <div style={{ 
          marginTop: '32px',
          padding: '16px',
          backgroundColor: '#f7fafc',
          borderRadius: '8px'
        }}>
          <p style={{ fontSize: '14px', color: '#718096', marginBottom: '8px' }}>
            <strong>Tech Stack:</strong>
          </p>
          <p style={{ fontSize: '14px', color: '#718096' }}>
            React + TypeScript • Vite • Turborepo • Express • React Native
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
