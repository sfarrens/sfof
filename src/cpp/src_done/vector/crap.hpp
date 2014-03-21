#ifndef _DATAXXX_HPP_
#define _DATAXXX_HPP_


#include <iostream>
#include <stdlib.h>
#include <math.h>
//#define NDEBUG // uncomment to remove checking of assert()
#include <assert.h>
#define DEFAULT_ALLOC 2



template <class ElType>
class new_matrix
{
  new_vector<ElType> *m;
  int rows,cols;
public:
  new_matrix();
  new_matrix( int r, int c);
  new_matrix(const new_matrix<ElType> &s);
  ~new_matrix();
  void set(ElType value , int r , int c){m[r][c]=value;};
  new_matrix& operator =(const new_matrix<ElType>& s);
  new_vector<ElType>& operator[](const int i);
  new_vector<ElType> operator*(const new_vector<ElType>&);
  friend new_matrix<ElType>  operator*(const ElType&, const new_matrix<ElType>&);
  friend new_matrix<ElType> operator*(const new_matrix<ElType>&, const ElType&);
  new_matrix<ElType> operator*(const new_matrix<ElType>& a);
  new_matrix<ElType> operator+(const new_matrix<ElType>& a);
  new_matrix<ElType> operator-(const new_matrix<ElType>& a);
  new_matrix<ElType> transpose();
  //new_matrix<ElType> inverse();
  friend ostream& operator<<(ostream& s,new_matrix<ElType>& m);
  friend void ludcmp(new_matrix<ElType>& a,new_vector<int>& indx,double &d);
  friend void lubksb(new_matrix<ElType>&a,new_vector<int>& indx,new_vector<ElType>&b);
  

};
template <class ElType>
new_matrix<ElType>::new_matrix()
{
	m = new new_vector<ElType>[DEFAULT_ALLOC];
	assert(m !=0);
	rows=cols=DEFAULT_ALLOC;
	for(int i=0;i<rows;i++)
	{
		new_vector<ElType> v;
		m[i]= v;
	}
}

template <class ElType>
new_matrix<ElType>::new_matrix(int r, int c)
{
	m= new new_vector<ElType>[r];
	assert(m != 0);
	rows=r;
	cols=c;
	for(int i=0;i<r;i++)
	{
		new_vector<ElType> v(cols);
		m[i]=v;
	}
}
template <class ElType>
new_matrix<ElType>::new_matrix(const new_matrix<ElType> &s)
{
	int i;
	rows=s.rows;
	m = new new_vector<ElType>[rows];
	assert(m!=0);
	cols =s.cols;
	for(i=0;i<rows;i++)
	{
	  m[i]=s.m[i];
	}
}
template <class ElType>
new_matrix<ElType>::~new_matrix()
{
	delete [] m;
}

template <class ElType>
new_matrix<ElType>& new_matrix<ElType>::operator =(const new_matrix<ElType> &s)
{
	if(this != &s)
	{
		delete []m;
		rows= s.rows;
		cols=s.cols;
		m = new new_vector<ElType>[rows];
		assert(m !=0);
		for(int i=0;i<rows;i++) m[i]=s.m[i];
	}
	return *this;
}
template <class ElType>
new_vector<ElType>& new_matrix<ElType>::operator[](const int i)
{
	assert(i>=0 && i < rows);
	return m[i];
}
template <class ElType>
new_vector<ElType> new_matrix<ElType>::operator*(const new_vector<ElType>& v)
{
	int i,j;
	assert(cols == v.len);
	new_vector<ElType> ans(rows);
	for(i=0;i<rows;i++)
	{
		ans.data[i]=0.0;
		for(j=0;j<cols;j++) ans.data[i] += m[i][j]*v.data[j];
	}
	return ans;
}
template <class ElType>
new_matrix<ElType> operator*(const ElType& x,const new_matrix<ElType>& s)
{
	new_matrix<ElType> ans(s.rows,s.cols);
	for(int i=0;i<ans.rows;i++)
	  {
		ans.m[i]= x*s.m[i];
	  }
	return ans;
}
template <class ElType>
new_matrix<ElType> new_matrix<ElType>::transpose()
{
  new_matrix<ElType> ans(cols,rows);
  for(int i=0;i<rows;i++)
	{
	  for(int j=0;j<cols;j++) ans[j][i]=m[i][j];
	  }
     return ans;
}
template <class ElType>
new_matrix<ElType> operator*(const new_matrix<ElType>& s,const ElType& x)
{
	new_matrix<ElType> ans(s.rows,s.cols);
	for(int i=0;i<ans.rows;i++)
	  {
		ans.m[i]= x*s.m[i];
	  }
	return ans;
}
template <class ElType>
new_matrix<ElType>  new_matrix<ElType> ::operator*(const new_matrix<ElType>&  a)
{

	assert(cols == a.rows);

	new_matrix<ElType>  ans(rows,a.cols);
	for(int i=0;i<rows;i++)
	{
		for(int j=0;j<a.cols;j++)
		{
			ans.m[i][j]=0.0;
			for(int k=0;k<cols;k++)
			{
				ans.m[i][j] += m[i][k]*a.m[k][j];
			}
		}
	}
	return ans;
}
template <class ElType>
new_matrix<ElType>  new_matrix<ElType> ::operator+(const new_matrix<ElType> & a)
{
	int i,j;

	assert(rows== a.rows);
	assert(cols== a.cols);

	new_matrix<ElType>  ans(a.rows,a.cols);
	for(i=0;i<a.rows;i++)
	{
		for(j=0;j<a.cols;j++)
		  {
			ans.m[i][j] = m[i][j] + a.m[i][j];  //faster than assigning new_vectors?
		}
	}
	return ans;
}
template <class ElType>
new_matrix<ElType> new_matrix<ElType>::operator-(const new_matrix<ElType>& a)
{
	int i,j;
	assert(rows == a.rows);
	assert(cols == a.cols);
	new_matrix ans(rows,cols);
	for(i=0;i<rows;i++)
	{
		for(j=0;j<cols;j++)
		ans.m[i][j] = m[i][j] - a.m[i][j];
	}
	return ans;
}
template <class ElType>
ostream& operator<<(ostream& s,new_matrix<ElType>& m)
{
	for(int i=0; i<m.rows;i++) s << m[i];
	return s;
}

#define TINY 1.0e-20;
//we assume fabs(ElType) is defined
//assignment of doubles to ElType is defined
template <class ElType>
void ludcmp(new_matrix<ElType>& a, new_vector<int>& indx,double& d)
{
	int i,imax,j,k;
	ElType  big,dum,sum,temp;
	int n=a.rows;
	new_vector<ElType> vv(n);
	assert(a.rows == a.cols);
	d=1.0;
	for (i=0;i<n;i++)
	{
		big=0.0;
		for (j=0;j<n;j++) if ((temp=fabs(a[i][j])) > big) big=temp;
		if (big == 0.0) cerr << "Singular new_matrix in routine LUDCMP" << endl;
		vv[i]=1.0/big;
	}
	for (j=0;j<n;j++)
	{
		for (i=0;i<j;i++)
		{
			sum=a[i][j];
			for (k=0;k<i;k++) sum -= a[i][k]*a[k][j];
			a[i][j]=sum;
		}
		big=0.0;
		for (i=j;i<n;i++)
		{
			sum=a[i][j];
			for (k=0;k<j;k++) sum -= a[i][k]*a[k][j];
			a[i][j]=sum;
			if ( (dum=vv[i]*fabs(sum)) >= big)
			{
				big=dum;
				imax=i;
			}
		}
		if (j != imax)
		{
			for (k=0;k<n;k++)
			{
				dum=a[imax][k];
				a[imax][k]=a[j][k];
				a[j][k]=dum;
			}
			d = -(d);
			vv[imax]=vv[j];
		}
		indx[j]=imax;
		if (a[j][j] == 0.0) a[j][j]=TINY;
		if (j != n-1) {
			dum=1.0/(a[j][j]);
			for (i=j+1;i<n;i++) a[i][j] *= dum;
		}
	}
}
#undef TINY
template <class ElType>
void lubksb(new_matrix<ElType>& a,new_vector<int>& indx,new_vector<ElType>& b)
{
	int i,ip,j;
	ElType sum;
	int n=a.rows;
	for (i=0;i<n;i++)
	{
		ip=indx[i];
		sum=b[ip];
		b[ip]=b[i];
		for (j=0;j<=i-1;j++) sum -= a[i][j]*b[j];
		b[i]=sum;
	}
	for (i=n-1;i>=0;i--)
	{
		sum=b[i];
		for (j=i+1;j<n;j++) sum -= a[i][j]*b[j];
		b[i]=sum/a[i][i];
	}
}
  
#endif
