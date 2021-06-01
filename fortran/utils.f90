
!> Utility module description goes here!
!! This is a continuation line for the module description.

!> @author J. Kaye
!> @version 0.0 

module utils

contains
  
  !> Evaluate the function \f$ (1-e^{-x})/x \f$ using
  !! a numerically stable method when the exponent is close to unity.
  !! @param[in] x point to evaluate the function
  !! @param[out] val resulting value

  subroutine evalexpfun(x,val)

    implicit none
    real *8 x,val
    
    integer i
    real *8 one,x1,c

    one = 1.0d0

    if (x>1.0d-1) then

       val = (one-exp(-x))/x

    else

       val = one
       c = one
       x1 = x
       do i=1,10
          c = c*(i+1)
          val = val + ((-1)**i)*x1/c
          x1 = x1*x
       enddo

    endif

  end subroutine evalexpfun

end module utils
